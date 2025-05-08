# Dataset directory in local device
data_dir = "/content/drive/MyDrive/Datasets/Final"

# Check if the dataset exists
import os
if not os.path.exists(data_dir):
    print("Dataset folder not found. Please check your Google Drive directory.")
else:
    print(f"Dataset folder found at: {data_dir}")

import torch
import torch.nn as nn
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image

# Dataset class
class FloorPlanDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        self.images = os.listdir(data_dir)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = os.path.join(self.data_dir, self.images[idx])
        image = Image.open(img_path).convert("RGB")
        if self.transform:
            image = self.transform(image)
        return image

# Generator
class Generator(nn.Module):
    def __init__(self, noise_dim, img_channels):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(noise_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, img_channels * 64 * 64),
            nn.Tanh()
        )

    def forward(self, x):
        return self.model(x).view(x.size(0), 3, 64, 64)

# Discriminator
class Discriminator(nn.Module):
    def __init__(self, img_channels):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(img_channels * 64 * 64, 1024),
            nn.LeakyReLU(0.2),
            nn.Linear(1024, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x.view(x.size(0), -1))

# Hyperparameters
noise_dim = 100
img_channels = 3
batch_size = 64
lr = 0.0002
epochs = 100

# Transformations
transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Load dataset
dataset = FloorPlanDataset(data_dir, transform=transform)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Initialize models
generator = Generator(noise_dim, img_channels).cuda()
discriminator = Discriminator(img_channels).cuda()

# Loss and Optimizers
criterion = nn.BCELoss()
optim_G = torch.optim.Adam(generator.parameters(), lr=lr, betas=(0.5, 0.999))
optim_D = torch.optim.Adam(discriminator.parameters(), lr=lr, betas=(0.5, 0.999))

# Training the GAN
os.makedirs("generated", exist_ok=True)
for epoch in range(epochs):
    for real_images in dataloader:
        real_images = real_images.cuda()
        batch_size = real_images.size(0)

        # Train Discriminator
        noise = torch.randn(batch_size, noise_dim).cuda()
        fake_images = generator(noise)
        real_labels = torch.ones(batch_size, 1).cuda()
        fake_labels = torch.zeros(batch_size, 1).cuda()

        real_loss = criterion(discriminator(real_images), real_labels)
        fake_loss = criterion(discriminator(fake_images.detach()), fake_labels)
        d_loss = real_loss + fake_loss

        optim_D.zero_grad()
        d_loss.backward()
        optim_D.step()

        # Train Generator
        g_loss = criterion(discriminator(fake_images), real_labels)

        optim_G.zero_grad()
        g_loss.backward()
        optim_G.step()

    print(f"Epoch [{epoch+1}/{epochs}] | D Loss: {d_loss.item():.4f} | G Loss: {g_loss.item():.4f}")

from transformers import pipeline
from torchvision.utils import save_image  # Import save_image
import os  # For directory management

# Load zero-shot classification model
print("Loading NLP model for prompt validation...")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define relevant topics for floor plans
relevant_topics = ["floor plan", "architecture", "building design", "room layout"]

# Ensure the 'generated/' directory exists
if not os.path.exists("generated"):
    os.makedirs("generated")

# Function to validate prompt and generate image
def validate_and_generate(prompt):
    result = classifier(prompt, candidate_labels=relevant_topics)
    max_score = max(result["scores"])
    print(f"Prompt relevance scores: {result['scores']}")

    if max_score < 0.001:
        print("The prompt is not related to floor plans. Please provide a valid prompt.")
        return

    # Generate image if prompt is valid
    noise = torch.randn(1, noise_dim).cuda()
    generated_image = generator(noise)
    save_image(generated_image, "generated/generated_prompt_based_image.png", normalize=True)
    print("Generated image based on the prompt has been saved at 'generated/generated_prompt_based_image.png'!")

# Example prompts
valid_prompt = "Design a floor plan for a 3-bedroom house with a kitchen and a living room."
invalid_prompt = "Generate a picture of a sunset over mountains."

# Test the model
user_prompt = input("Enter a prompt related to a floor plan: ")
validate_and_generate(user_prompt)