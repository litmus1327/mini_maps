import qrcode

# === USER INPUT ===
site_name = "McLarenFentonED"  # <-- update this for each facility
base_url = "https://yourlookupsite.com"  # <-- replace with your actual lookup tool URL

# === GENERATE QR URL ===
qr_url = f"{base_url}/?site={site_name}"

# === GENERATE QR CODE ===
qr = qrcode.make(qr_url)

# === SAVE QR CODE IMAGE ===
output_filename = f"{site_name}_QR.png"
qr.save(output_filename)

print(f"✅ QR code generated for {site_name}: {output_filename}")
print(f"🌐 Encoded URL: {qr_url}")
