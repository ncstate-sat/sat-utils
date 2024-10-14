This example uses a SATLogger class, but relies on a call to the logging setup function.

Again, this relies on the applications to make a call to the logging setup function in their entrypoint,
but then the existing `SATLogger` class can be used to instantiate loggers throughout the app's modules.
They actually could just as easily use `logging.getLogger` to instantiate a logger; the `SATLogger` here doesn't
really do anything, all of the configuration is handled in the setup function.
