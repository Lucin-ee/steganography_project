from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def calculate_mean_and_std(histogram, total_pixels):


    mean = sum(histogram[i] * i for i in range(len(histogram))) / total_pixels
    variance = sum(histogram[i] * (i - mean) ** 2 for i in range(len(histogram))) / total_pixels
    std_dev = np.sqrt(variance)
    return mean, std_dev

def get_lsb_histogram(image_path, lsb_count=1):

   

    if not (1 <= lsb_count <= 4):
        raise ValueError("lsb_count must be between 1 and 4")

    # Open the image and load pixels
    img = Image.open(image_path)
    pixels = np.array(img)

    # Initialize histograms for each color channel
    r_hist = [0] * (1 << lsb_count)  # 2^lsb_count bins for Red
    g_hist = [0] * (1 << lsb_count)  # 2^lsb_count bins for Green
    b_hist = [0] * (1 << lsb_count)  # 2^lsb_count bins for Blue

    total_pixels = pixels.shape[0] * pixels.shape[1]

    # Iterate through all pixels
    for y in range(pixels.shape[0]):
        for x in range(pixels.shape[1]):
            r, g, b = pixels[y, x]

            # Extract the last `lsb_count` bits of each color channel
            r_lsb = r & ((1 << lsb_count) - 1)
            g_lsb = g & ((1 << lsb_count) - 1)
            b_lsb = b & ((1 << lsb_count) - 1)

            # Increment the corresponding bins in the histograms
            r_hist[r_lsb] += 1
            g_hist[g_lsb] += 1
            b_hist[b_lsb] += 1

    # Calculate mean and standard deviation for each channel
    r_mean, r_std = calculate_mean_and_std(r_hist, total_pixels)
    g_mean, g_std = calculate_mean_and_std(g_hist, total_pixels)
    b_mean, b_std = calculate_mean_and_std(b_hist, total_pixels)

    # Prepare x-axis labels (binary representations of bit patterns)
    x_labels = [f"{bin(i)[2:].zfill(lsb_count)}" for i in range(1 << lsb_count)]

    # Create the histogram plot
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.bar(x_labels, r_hist, color='red', alpha=0.7)
    plt.title(f'Red Channel - Last {lsb_count} Bits')
    plt.xlabel('Bit Pattern')
    plt.ylabel('Frequency')

    plt.subplot(1, 3, 2)
    plt.bar(x_labels, g_hist, color='green', alpha=0.7)
    plt.title(f'Green Channel - Last {lsb_count} Bits')
    plt.xlabel('Bit Pattern')

    plt.subplot(1, 3, 3)
    plt.bar(x_labels, b_hist, color='blue', alpha=0.7)
    plt.title(f'Blue Channel - Last {lsb_count} Bits')
    plt.xlabel('Bit Pattern')

    # Adjust layout
    plt.tight_layout()

    # Save the plot as a PNG file
    output_filename = f"histogram_{image_path.split('.')[0]}_{lsb_count}.png"
    plt.savefig(output_filename)
    plt.close()  # Close the plot to free up memory

    # Print the results
    print(f"Histogram saved as {output_filename}")
    print(f"Red Channel - Mean: {r_mean:.2f}, Std Dev: {r_std:.2f}")
    print(f"Green Channel - Mean: {g_mean:.2f}, Std Dev: {g_std:.2f}")
    print(f"Blue Channel - Mean: {b_mean:.2f}, Std Dev: {b_std:.2f}")