# Main script for runnning things
import argparse
BATCH_TEMPLATE = """\
#!/bin/bash

#SBATCH --model {model_name}
#SBATCH --feature-exctraction {feature_model_name}
#SBATCH --seed {seed_nb}
#SBATCH --n_prior_included {nb_included}
#SBATCH --n_prior_excluded {nb_excluded}

srun automatic-screening batch {args}
"""

DEFAULT_N_PRIOR_INCLUDED = 5
DEFAULT_N_PRIOR_EXCLUDED = 5
DEFAULT_FEATURE_EXTRACTION = "Word2Vec"
DEFAULT_MODEL = "Log_Reg"

def _simulate_parser():
    parser = argparse.ArgumentParser(
        prog='AutomaticScreening',
        description='Runs an automatic screening'
    )

    subparsers = parser.add_subparsers(dest='command')

    parser.add_argument("--n_prior_included",
                        default=DEFAULT_N_PRIOR_INCLUDED,
                        type=int,
                        help="Sample n prior included papers"
                        f"Default is {DEFAULT_N_PRIOR_INCLUDED}")
    
    parser.add_argument("--n_prior_included",
                        default=DEFAULT_N_PRIOR_EXCLUDED,
                        type=int,
                        help="Sample n prior excluded papers"
                        f"Default is {DEFAULT_N_PRIOR_EXCLUDED}")
    
    parser.add_argument("-f",
                        "--feature_extraction",
                        type=str,
                        default=DEFAULT_FEATURE_EXTRACTION,
                        help="Feature extraction method"
                        f"Default is {DEFAULT_FEATURE_EXTRACTION}")
    
    parser.add_argument("-m",
                        "--model",
                        type=str,
                        default=DEFAULT_MODEL,
                        help="The prediction model to use."
                        f"Default is {DEFAULT_MODEL}")
    
    parser.add_argument("--seed",
                        default=101,
                        type=int,
                        help="Seed for models.")
    
    return parser

def _eval_parser():
    """Returns parser for evaluation

    Adds relevant arguments for an evaluation parsing. 
    When a user wishes to run an evaluation given a dataset, 
    he/she needs to provide, which feature-extraction and classifier 
    he/she wants to evaluate.

    Args:
    
    """
    parser = argparse.ArgumentParser(
        prog='AutomaticScreening',
        description='Runs an evaluation on a given dataset and model. Outputs'
        'Outputs its performance.'
    )

    parser.add_argument("-f",
                        "--feature_extraction",
                        type=str,
                        default=DEFAULT_FEATURE_EXTRACTION,
                        help="Feature extraction method"
                        f"Default is {DEFAULT_FEATURE_EXTRACTION}")
    
    parser.add_argument("-m",
                        "--model",
                        type=str,
                        default=DEFAULT_MODEL,
                        help="The prediction model to use."
                        f"Default is {DEFAULT_MODEL}")
    
    parser.add_argument("--seed",
                        default=101,
                        type=int,
                        help="Seed for models.")
    
    return parser

def _fit_parser():
    """Returns a parser to fit for a review.

    Adds relevant arguments for a fitting parsing.
    
    """
    parser = argparse.ArgumentParser(
        prog='AutomaticScreening',
        description='Given a review, a model will fit to the review.'
    )

    parser.add_argument("--n_prior_included",
                    default=DEFAULT_N_PRIOR_INCLUDED,
                    type=int,
                    help="Sample n prior included papers"
                    f"Default is {DEFAULT_N_PRIOR_INCLUDED}")
    
    parser.add_argument("--n_prior_included",
                        default=DEFAULT_N_PRIOR_EXCLUDED,
                        type=int,
                        help="Sample n prior excluded papers"
                        f"Default is {DEFAULT_N_PRIOR_EXCLUDED}")
    
    parser.add_argument("-f",
                        "--feature_extraction",
                        type=str,
                        default=DEFAULT_FEATURE_EXTRACTION,
                        help="Feature extraction method"
                        f"Default is {DEFAULT_FEATURE_EXTRACTION}")
    
    parser.add_argument("-m",
                        "--model",
                        type=str,
                        default=DEFAULT_MODEL,
                        help="The prediction model to use."
                        f"Default is {DEFAULT_MODEL}")
    
    parser.add_argument("--seed",
                        default=101,
                        type=int,
                        help="Seed for models.")
    
def _predict_parser():
    """Returns a parser to predict in a review.

    Adds relevant arguments for a prediction parsing.
    When a user 
    
    """
    parser = argparse.ArgumentParser(
        prog='AutomaticScreening',
        description='Given a review, a model will fit to the review.'
    )
    # This probably needs to be a path to a trained model
    parser.add_argument("-m",
                        "--model",
                        type=str,
                        default=DEFAULT_MODEL,
                        help="The prediction model to use."
                        f"Default is {DEFAULT_MODEL}")


def _method_parser():
    parser = argparse.ArgumentParser(description='Run a command from Silvi Automatic-Screening')
    
    subparsers = parser.add_subparsers(dest='command')

    eval_parser = subparsers.add_parser('eval', parents=[_simulate_parser()])
    fit_parser = subparsers.add_parser('fit', parents=[_simulate_parser()])
    predict_parser = subparsers.add_parser('predict')

    # if args.command == 'eval':
    #     eval_parser.add_argument("-m",
    #                              "--model",
    #                              type=str,
    #                              default=DEFAULT_MODEL,
    #                              help="The prediction model to use."
    #                              f"Default is {DEFAULT_MODEL}")
    # return 

def run_simulation(argv):

    parser = _simulate_parser()
    args = parser.parse_args(argv)