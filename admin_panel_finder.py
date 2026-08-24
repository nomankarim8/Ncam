#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Enhanced Admin Panel Finder Tool
# Original by: nomankarim8
# Improved: Added multithreading for speed, HTTPS support, status code display,
#           progress bar, better error handling, and user-agent header.
# For Legal & Ethical Use Only (e.g., on sites you own or have permission to test)
 
  
import urllib.request
from urllib.error import HTTPError, URLError
import concurrent.futures
import sys
  
def credit():
    banner = """
🛡️=======================================🛡️
|     Enhanced Admin Panel Finder Tool    |
|       Original by: nomankarim8          |
|      Improved for better performance    |
|      For Legal & Ethical Use Only       |
🛡️=======================================🛡️
"""
    print(banner)

def check_path(base_url, path, opener, results):
    url = f"{base_url.rstrip('/')}/{path.strip().lstrip('/')}"
    try: 
        resp = opener.open(url)
        status = resp.code
        if status == 200:
            results.append(f"[FOUND {status}] => {url}")
        elif 300 <= status < 400:
            location = resp.getheader('Location', 'Unknown')
            results.append(f"[REDIRECT {status}] => {url} -> {location}")

    except HTTPError as e:
        if e.code == 401:
            results.append(f"[AUTH REQUIRED {e.code}] => {url}")
        
    except URLError:
        pass  
    except Exception:
        pass
 
def find_admin():
    try:
        with open("link.txt", "r") as f:
            paths = [line for line in f if line.strip()]
        
        if not paths:
            print("Warning: 'link.txt' is empty!")
            return
        
        site = input("Enter Site Name (ex: example.com or www.example.com): ").strip()
        if not site:
            print("Error: No site entered!")
            return
        
        protocol = input("Use HTTPS? (y/n, default n): ").strip().lower()
        use_https = protocol == 'y'
        base_proto = "https://" if use_https else "http://"
        base_url = f"{base_proto}{site}"
        
        threads_input = input("Number of threads (default 20): ").strip()
        max_threads = int(threads_input) if threads_input.isdigit() else 20
        
        print(f"\nScanning {base_url} with {len(paths)} paths using {max_threads} threads...\n")
        
      
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')]
        
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = [executor.submit(check_path, base_url, path, opener, results) for path in paths]
          
            completed = 0
            for future in concurrent.futures.as_completed(futures):
                completed += 1
                sys.stdout.write(f"\rProgress: {completed}/{len(paths)} paths checked")
                sys.stdout.flush()
        
        print("\n\nResults:")
        found = [r for r in results if "FOUND" in r or "AUTH" in r or "REDIRECT" in r]
        if found:
            for res in found:
                print(res)
        else:
            print("No potential admin panels found (200/401/3xx).")
        
       
        others = [r for r in results if r not in found]
        if others:
            print(f"\nOther interesting responses ({len(others)}):")
            for res in others[:20]:  
                print(res)
            if len(others) > 20:
                print("... (truncated)")

    except FileNotFoundError:
        print("Error: 'link.txt' not found! Create it with one path per line (e.g., admin/, admin/login.php).")
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

credit()
find_admin()