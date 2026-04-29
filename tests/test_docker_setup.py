#!/usr/bin/env python3
"""Tests for Docker setup validation (TDD - these should fail before implementation)"""

import os
import re
import subprocess
import pytest

def test_dockerfile_exists():
    """CA-01: Dockerfile should exist"""
    assert os.path.exists("Dockerfile"), "Dockerfile not found"

def test_dockerfile_uses_python311_slim():
    """CA-01: Dockerfile should use python:3.11-slim as base"""
    with open("Dockerfile", "r") as f:
        content = f.read()
    assert "python:3.11-slim" in content, "Dockerfile must use python:3.11-slim base image"

def test_dockerfile_runs_rustchain_miner():
    """CA-02: Dockerfile should run rustchain_universal_miner.py"""
    with open("Dockerfile", "r") as f:
        content = f.read()
    assert "rustchain_universal_miner.py" in content, "Dockerfile must reference rustchain_universal_miner.py"

def test_dockerfile_has_wallet_env():
    """CA-03: Dockerfile should have WALLET environment variable"""
    with open("Dockerfile", "r") as f:
        content = f.read()
    assert "WALLET" in content, "Dockerfile must define WALLET environment variable"

def test_dockerfile_has_node_url_env():
    """CA-03: Dockerfile should have NODE_URL environment variable"""
    with open("Dockerfile", "r") as f:
        content = f.read()
    assert "NODE_URL" in content, "Dockerfile must define NODE_URL environment variable"

def test_dockerfile_has_healthcheck():
    """CA-04: Dockerfile should have HEALTHCHECK instruction"""
    with open("Dockerfile", "r") as f:
        content = f.read()
    assert "HEALTHCHECK" in content, "Dockerfile must include HEALTHCHECK instruction"

def test_docker_compose_exists():
    """CA-06: docker-compose.yml should exist"""
    assert os.path.exists("docker-compose.yml"), "docker-compose.yml not found"

def test_docker_compose_uses_ghcr_image():
    """CA-05: docker-compose.yml should reference ghcr.io image"""
    with open("docker-compose.yml", "r") as f:
        content = f.read()
    assert "ghcr.io" in content, "docker-compose.yml must reference ghcr.io image"

def test_docker_compose_has_environment_section():
    """CA-06: docker-compose.yml should have environment variables"""
    with open("docker-compose.yml", "r") as f:
        content = f.read()
    assert "WALLET" in content, "docker-compose.yml must have WALLET environment variable"
    assert "NODE_URL" in content, "docker-compose.yml must have NODE_URL environment variable"

def test_docker_compose_has_healthcheck():
    """CA-04: docker-compose.yml should have health check configured"""
    with open("docker-compose.yml", "r") as f:
        content = f.read()
    assert "healthcheck" in content.lower(), "docker-compose.yml must include healthcheck configuration"

def test_readme_has_docker_section():
    """CA-07: README.md should have Docker quick start section"""
    with open("README.md", "r") as f:
        content = f.read()
    assert "docker" in content.lower(), "README.md must include Docker section"
    assert "WALLET" in content, "README.md must document WALLET environment variable"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
