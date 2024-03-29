#!/usr/bin/env python3
import os, re, phonetisaurus, json
from bottle import route, run, template, request, response
from collections import namedtuple, defaultdict

# Globals, oh no!
_g2pmodel = None
_lexicon = defaultdict(list)

###############################
# Utilities
def _phoneticize(model, args):
    """
    Python wrapper function for g2p.
    """

    results = model.Phoneticize(
        args.token,
        args.nbest,
        args.beam,
        args.thresh,
        args.write_fsts,
        args.accumulate,
        args.pmass
    )

    pronunciations = []
    for result in results:
        pronunciation = [model.FindOsym(u) for u in result.Uniques]
        yield "{0}".format(" ".join(pronunciation))

def _loadLexicon(lexiconfile):
    with open(lexiconfile, "r", encoding="utf-8") as ifp:
        for entry in ifp:
            word, pron = re.split(r"\t", entry.strip())
            _lexicon[word].append(pron)
    return

def _defaultArgs(userargs):
    args = namedtuple('args', [
        'token', 'nbest', 'beam', 'thresh', 'write_fsts',
        'accumulate', 'pmass'
    ])

    args.token = ""
    args.nbest = int(userargs.get("nbest", 2))
    args.beam = int(userargs.get("beam", 500))
    args.thresh = float(userargs.get("thresh", 10.))
    args.pmass = float(userargs.get("pmass", 0.0))
    args.write_fsts = False
    args.accumulate = userargs.get("accumulate", False)
    return args
###############################

@route('/phoneticize/list', method="POST")
def PhoneticizeList():
    """Phoneticize a list of words."""
    default_args = _defaultArgs(request.forms)

    wlist = request.files.get("wordlist")

    words = re.split(r"\n", wlist.file.read().decode("utf-8"))

    lexicon = []
    for word in words:
        if re.match(r"^\s*$", word) or "<" in word or "[" in word:
            continue

        default_args.token = word.lower()
        if default_args.token in _lexicon:
            for pronunciation in _lexicon[default_args.token]:
                lexicon.append("{0}\t{1}".format(word, pronunciation))
        else:
            for pronunciation in _phoneticize(_g2pmodel, default_args):
                lexicon.append("{0}\t{1}".format(word, pronunciation))

    response.set_header('Access-Control-Allow-Origin', '*')

    return "\n".join(lexicon).encode("utf-8")


if __name__ == '__main__':
    import sys, argparse

    example = "{0} --host localhost --port 8080"\
              " --model g2p.fst --lexicon ref.lexicon"
    example = example.format(sys.argv[0])
    parser = argparse.ArgumentParser(description=example)
    parser.add_argument("--host", "-hs", help="IP to host the service on.",
                        default="localhost")
    parser.add_argument("--port", "-p", help="Port to use for hosting.",
                        default=8080, type=int)
    parser.add_argument("--model", "-m", help="Phonetisaurus G2P model.",
                        required=True)
    parser.add_argument("--lexicon", "-l", help="Reference lexicon.",
                        required=True)
    parser.add_argument("--verbose", "-v", help="Verbose mode.",
                        default=False, action="store_true")
    args = parser.parse_args()

    if args.verbose:
        for key, val in
