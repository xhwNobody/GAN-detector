import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=str, help='data directory')
    parser.add_argument('--batch-size', type=int, help='batch size')
    parser.add_argument('--gpu', type=int, default=0)
    return parser.parse_args()