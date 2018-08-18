import re


def get_rom_name():
    ''' Get ROM name from line and strip characters returns from wget '''
    rom = line[slash_position+1:]
    rom = rom.strip("\n")
    rom = strip_hyphens_and_percentages(rom)
    rom = replace_brackets(rom)
    return rom

def strip_hyphens_and_percentages(rom):
    ''' Strip the hyphens and percentage signs from ROM filenames
        returned from wget when file was generated. '''
    rom = rom.replace("-", " ").replace("%20", " ")
    return rom

def replace_brackets(rom):
    ''' Replace brackets that does not show correctly in ROM filenames.
        "%5B and %5d was returned instead of brackets [] '''
    rom = rom.replace("%5b", "[").replace("%5d", "]")
    return rom


name_and_length = {}

with open("wgetlog.txt", "r") as wget: # Log file generated by wget
    read_data = wget.readlines()

    for line in read_data:

        if line.startswith("--"):
        # Rom name begins with line that starts with "--"
            slash_position = line.rfind("/")
            rom_name = get_rom_name()

        if line.startswith("Length: "):
        # ROM size starts with line that begins with "Length: "

            # Regex that searches for spaces and returns length of ROM
            for m in re.finditer(" ", line):
                print("Space at: ", m.start(), m.end())
                size_of_rom = line[8:m.end()]
                if size_of_rom != "":
                    break

            if rom_name == "" or rom_name.startswith("?"):
                continue
            else:
                name_and_length[rom_name] = size_of_rom.strip()

print(name_and_length)

f = open('Rom Sizes.txt', 'w')
for k, v in name_and_length.items():
    f.write(str(k) + '\t' + str(v) + '\n')
f.close()
