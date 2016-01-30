from core.application import *
import sys


# Entry point
def main(argv):

    # Create the application and pass in the arguments
    app = Application(argv)

    # Run the application, and exit when finished
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
