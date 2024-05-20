from pathlib import Path

def main():
    # Prompt the user for input and output filenames
    input_filename = Path(__file__).parent / "JackAndJillEncoded.txt"
    #input_filename = input("Enter the source filename: ").strip()
    output_filename = Path(__file__).parent / "JackAndJillDecoded.txt"
    #output_filename = input("Enter the target filename: ").strip()

    try:
        # Open the encoded file for reading
        with open(input_filename, "rb") as input_file:
            # Read the content of the encoded file as bytes
            encoded_content = input_file.read()

        # Decode the content
        decoded_content = bytearray()

        for byte in encoded_content:
            # Subtract 2 from the value of each byte to decode
            decoded_content.append(byte - 2)

        # Open the output file for writing the decoded content
        with open(output_filename, "wb") as output_file:
            # Write the decoded content to the output file
            output_file.write(decoded_content)

        print("File decoded successfully. Decoded content saved to", output_filename)

    except FileNotFoundError:
        print("File not found. Please enter valid filenames.")


if __name__ == "__main__":
    main()
