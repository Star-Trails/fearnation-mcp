"""CLI entry point for fearnation-mcp.

Run with: `fearnation-mcp` or `python -m fearnation_mcp`.
"""

from __future__ import annotations

import logging

from fearnation_mcp.server import run


def main() -> None:
    """Run the MCP server over stdio transport."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        handlers=[logging.StreamHandler()],  # stderr by default
    )
    run()


if __name__ == "__main__":
    main()
