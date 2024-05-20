from pathlib import Path

def main():
    # Prompt the user for input and output filenames
    input_filename = Path(__file__).parent / "JackAndJill.txt"
    #input_filename = input("Enter the source filename: ").strip()
    output_filename = Path(__file__).parent / "JackAndJillEncoded.txt"
    #output_filename = input("Enter the target filename: ").strip()

    try:
        # Open the input file for reading
        with open(input_filename, "rb") as input_file:
            # Read the content of the input file as bytes
            input_content = input_file.read()

        # Encode the content
        encoded_content = bytearray()

        for byte in input_content:
            # Add 2 to the value of each byte to encode
            encoded_content.append(byte + 2)

        # Open the output file for writing the encoded content
        with open(output_filename, "wb") as output_file:
            # Write the encoded content to the output file
            output_file.write(encoded_content)

        print("File encoded successfully. Encoded content saved to", output_filename)

    except FileNotFoundError:
        print("File not found. Please enter valid filenames.")


if __name__ == "__main__":
    main()