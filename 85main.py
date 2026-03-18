import argparse

parser = argparse.ArgumentParser()

#Add command line argument
parser.add_argument("file_to_download", help="Url of the file to download")
parser.add_argument("output", help="Path to the output file")


#parse the argument
args = parser.parse_args()


#use the argument in your code
print(args.file_to_download)
print(args.output)