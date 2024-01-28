import os


if __name__ == '__main__':
    OUTPUT_DIRECTORY = 'state_machine_build'

    # output directory
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)
    os.chdir(OUTPUT_DIRECTORY)
    print("Hello, World")


