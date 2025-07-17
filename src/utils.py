# Utility functions for MCP server
# This file can be used to add utility functions for future enhancements

import os

def get_config_value(key: str, default: str = "") -> str:
    """Get configuration value from environment variables.
    
    Args:
        key: The environment variable key
        default: Default value if key is not found
        
    Returns:
        The configuration value or default
    """
    return os.getenv(key, default)