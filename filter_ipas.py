"""
Script to filter ipas from the audio-ipa aligned file.

Usage:
    filter_ipas.py --input-file=<i> --ipas-lst=<il>,<il> --output-file=<o>

Options:
    --input-file=<i>        Audio ipa aligned input file in `txt` format
    --ipas-lst=<il>,<il>        List of ipas you want to filter. Eg: mh,nh
    --output-file=<o>       Output file for the filtered audio-ipa aligned sentences
"""
from docopt import docopt
from filter import filter_ipas
from utils import read_file
from utils import write_file


if __name__ == "__main__":
    args = docopt(__doc__)

    input_file = args["--input-file"]
    ipas_lst = args["--ipas-lst"].split(',')
    output_file = args["--output-file"]

    ipas = read_file(input_file)

    filtered_sentences = [sent for item in ipas for sent in filter_ipas(item, ipas_lst)]

    write_file(output_file, filtered_sentences)
