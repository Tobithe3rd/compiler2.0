class Config:
    """Configuration class to manage global settings for the compiler."""

    def __init__(self):
        # Default settings
        self.output_file = "output.asm"
        self.debug = False

    def set_output_file(self, output_file):
        """Set the output file name."""
        self.output_file = output_file

    def enable_debug(self):
        """Enable debug mode."""
        self.debug = True

    def disable_debug(self):
        """Disable debug mode."""
        self.debug = False

    def get_output_file(self):
        """Get the output file name."""
        return self.output_file

    def is_debug_enabled(self):
        """Check if debug mode is enabled."""
        return self.debug
