#!/usr/bin/env python3
"""
QR Code Generator for https://suffix-decoding.github.io
"""

import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_H

def generate_qr_code(url: str, output_file: str) -> None:
    
    # Create QR code instance with custom settings
    qr = qrcode.QRCode(
        version=1,  # Version 1 is 21x21 pixels, will auto-adjust if needed
        error_correction=ERROR_CORRECT_M,  # Medium error correction (15% recovery)
        box_size=10,  # Size of each box in pixels
        border=4,  # Minimum border size (in boxes)
    )
    
    # Add the URL data
    qr.add_data(url)
    qr.make(fit=True)  # Automatically adjust version to fit the data
    
    # Create the image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code as PNG
    img.save(output_file)
    print(f"✅ QR code generated successfully!")
    print(f"📁 Saved as: {output_file}")
    print(f"🔗 URL encoded: {url}")
    
    # # Also generate a high-contrast version with custom colors
    # img_custom = qr.make_image(fill_color="#1a1a2e", back_color="#ffffff")
    # custom_output = "suffix_decoding_qr_custom.png"
    # img_custom.save(custom_output)
    # print(f"🎨 Custom color version saved as: {custom_output}")
    
    # return output_file, custom_output

if __name__ == "__main__":
    generate_qr_code("https://suffix-decoding.github.io", "./project_page.png")
    generate_qr_code("https://arxiv.org/abs/2411.04975", "./paper.png")
    generate_qr_code("https://github.com/snowflakedb/ArcticInference", "./code.png")
