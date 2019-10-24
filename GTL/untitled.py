import os

folder_path = "/Users/Abbatepaolo/Downloads/test_letters/Number"
output_path = "/Users/Abbatepaolo/Desktop/t"

# Iterating over folders and subdirectories to get all txt files
for subdir, dirs, files in os.walk(folder_path):
    for file in files:
        if ".txt" in file:

            # Getting txt path
            txt_path = os.path.join(subdir, file)

            # Reading file
            with open(txt_path, "r") as txt_open:

                # Splitting file in separate lines
                txt_lines = txt_open.read().splitlines()

                # Glyph name
                key = txt_lines[0]
                # Glyph structure
                val = txt_lines[2:]

                v = []

                for line in val:
                    x = line.replace("@", "#")
                    x = x.replace("&", "#")
                    x = x.replace("+", "#")
                    x = x.replace("%", "#")
                    x = x.replace("$", "#")
                    v.append(x)

                out_file = os.path.join(output_path, file)
                with open(out_file, "w") as f:
                    f.write(key)
                    f.write("\n")
                    f.write("")
                    f.write("\n")
                    for l in v:
                        f.write(l)
                        f.write("\n")