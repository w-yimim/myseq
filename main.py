from bioseq.SeqCal import gcContent, atContent, countBase, countBasesDict
from bioseq.SeqPattern import cpgSearch, enzTargetsScan
from bioseq.SeqMan import reverseSeq, complementSeq, reverseComplementSeq, dna2rna, dna2protein, loadCodons

def argparserLocal():
    from argparse import ArgumentParser
    ''' Argument parser for the command'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(title = 'command', description='Please choose commamd below:', dest='command')

    subparsers.required = True

    gc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    gc_command.add_argument('-s', '--seq', type =str, default=None, help='Provide sequence')

    countBases_command = subparsers.add_parser('countBases', help='Count number of each base')
    countBases_command.add_argument('-s', '--seq', type = str, default=None, help ='Provide sequence')
    countBases_command.add_argument('-r', '--revcomp', action = "store_true", help = 'Convet DNA to reverse-complementary')

    transcription_command = subparsers.add_parser('transcription', help = 'Convert DNA->RNA')
    transcription_command.add_argument('-s', '--seq', type = str, default = None, help ='Provide sequence')
    transcription_command.add_argument('-r', '--revcomp', action = "store_true", help = 'Convet DNA to reverse-complementary')

    translationtion_command = subparsers.add_parser('translation', help = "Convert DNA->Protein")
    translationtion_command.add_argument('-s', '--seq', type = str, default = None, help ='Provide sequence')
    translationtion_command.add_argument('-r', '--revcomp', action = "store_true", help = 'Convet DNA to reverse-complementary')

    enzTargetsScan_command = subparsers.add_parser('enzTargetsScan', help = "Find restriction enzyme")
    enzTargetsScan_command.add_argument('-s', '--seq', type = str, default = None, help ='Provide sequence')
    enzTargetsScan_command.add_argument('-e', '--enz', type = str, default = None, help ='Enzyme name')
    enzTargetsScan_command.add_argument('-r', '--revcomp', action = "store_true", help = 'Convet DNA to reverse-complementary')

    return parser
def main():
    parser = argparserLocal()
    args = parser.parse_args()
    
    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        print("Input ", args.seq)
        gcContent_result = gcContent(args.seq.upper())
        print('GC content =', gcContent_result)
    
    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        print("Input ", args.seq)
        if not args.revcomp:
            countBases_result = countBasesDict(args.seq.upper())
            print('countBases =', countBases_result)
        elif args.revcomp:
            countBases_result = reverseComplementSeq(args.seq.upper())
            countBases_result = countBasesDict(countBases_result)
            print('countBases =', countBases_result)
    
    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        print("Input ", args.seq)
        if not args.revcomp:
            transcription_result = dna2rna(args.seq.upper())
            print('Transcription =', transcription_result)
        elif args.revcomp:
            transcription_result = reverseComplementSeq(args.seq.upper())
            transcription_result = dna2rna(transcription_result)
            print('Transcription =', transcription_result)

    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h']))
        print("Input ", args.seq)
        if not args.revcomp:
            translation_result = dna2protein(args.seq.upper())
            print('Translation =', translation_result)
        elif args.revcomp:
            translation_result = reverseComplementSeq(args.seq.upper())
            translation_result = dna2protein(translation_result)
            print('Transcription =', translation_result)
    
    elif args.command == 'enzTargetsScan':
        if args.seq == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        print("Input ", args.seq)
        if not args.revcomp:
            sequence = args.seq.upper()
            enzTargetsScan_result  = enzTargetsScan(sequence, args.enz)
            print(f'{args.enz} = {enzTargetsScan_result}')
        elif args.revcomp:
            sequence = args.seq.upper()
            enzTargetsScan_result = reverseComplementSeq(sequence)
            enzTargetsScan_result  = enzTargetsScan(enzTargetsScan_result, args.enz)
            print(f'{args.enz} = {enzTargetsScan_result}')

    