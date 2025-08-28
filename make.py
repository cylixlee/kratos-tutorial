#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Build script to replace Makefile for kratos-tutorial project.
This script provides equivalent functionality to the original Makefile.
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


def find_proto_files(directory):
    """Find all .proto files in directory recursively"""
    proto_files = []
    dir_path = Path(directory)
    if dir_path.exists():
        for proto_file in dir_path.rglob("*.proto"):
            proto_files.append(str(proto_file).replace('\\', '/'))
    return proto_files


def run_command(cmd, shell=False):
    """Run command and raise exception on failure"""
    try:
        if isinstance(cmd, list):
            if sum(map(len, cmd)) >= 80:
                print('\n  '.join(cmd))
            else:
                print(' '.join(cmd))
        else:
            print(cmd)
        result = subprocess.run(cmd, shell=shell, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e.cmd}")
        print(f"Error output:\n  {e.stderr}")
        raise Exception(f"Command failed with exit code {e.returncode}") from e


def task_init():
    """Initialize environment by installing required tools"""
    tools = [
        "google.golang.org/protobuf/cmd/protoc-gen-go@latest",
        "google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest",
        "github.com/go-kratos/kratos/cmd/kratos/v2@latest",
        "github.com/go-kratos/kratos/cmd/protoc-gen-go-http/v2@latest",
        "github.com/google/gnostic/cmd/protoc-gen-openapi@latest",
        "go.uber.org/fx@latest"
    ]
    
    for tool in tools:
        run_command(['go', 'install', tool])


def task_config():
    """Generate internal proto files"""
    internal_proto_files = find_proto_files("internal")
    if not internal_proto_files:
        print("No internal proto files found")
        return
    
    cmd = [
        'protoc',
        '--proto_path=./internal',
        '--proto_path=./third_party',
        '--go_out=paths=source_relative:./internal'
    ] + internal_proto_files
    
    run_command(cmd)


def task_api():
    """Generate API proto files"""
    api_proto_files = find_proto_files("api")
    if not api_proto_files:
        print("No API proto files found")
        return
    
    cmd = [
        'protoc',
        '--proto_path=./api',
        '--proto_path=./third_party',
        '--go_out=paths=source_relative:./api',
        '--go-http_out=paths=source_relative:./api',
        '--go-grpc_out=paths=source_relative:./api',
        '--openapi_out=fq_schema_naming=true,default_response=false:.',
    ] + api_proto_files
    
    run_command(cmd)


def task_build():
    """Build the application"""
    # Create bin directory if it doesn't exist
    os.makedirs("bin", exist_ok=True)
    
    # Get version from git
    try:
        version_result = subprocess.run(['git', 'describe', '--tags', '--always'], 
                                      capture_output=True, text=True, check=True)
        version = version_result.stdout.strip()
    except subprocess.CalledProcessError:
        version = "unknown"
    
    cmd = [
        'go',
        'build',
        f'-ldflags=-X main.Version={version}',
        '-o', './bin/',
        './...'
    ]
    
    run_command(cmd)


def task_generate():
    """Run go generate and tidy"""
    run_command(['go', 'generate', './...'])
    run_command(['go', 'mod', 'tidy'])


def task_all_targets():
    """Run all targets"""
    task_api()
    task_config()
    task_generate()


def show_help():
    """Show help message"""
    help_text = """
Usage:
 python build.py [target]

Targets:
 init                   Install required tools
 config                 Generate internal proto files
 api                    Generate API proto files
 build                  Build the application
 generate               Run go generate and tidy
 all                    Run all targets (api, config, generate)
 help                   Show this help message
"""
    print(help_text)


def main():
    """Main function"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    target = sys.argv[1]
    
    try:
        if target == "init":
            task_init()
        elif target == "config":
            task_config()
        elif target == "api":
            task_api()
        elif target == "build":
            task_build()
        elif target == "generate":
            task_generate()
        elif target == "all":
            task_all_targets()
        elif target == "help":
            show_help()
        else:
            print(f"Unknown target: {target}")
            show_help()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()