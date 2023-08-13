#! /usr/bin/python
import os
import json
import shutil

def move_files( files, source_dir, destination_dir ):
    for i, f in enumerate( files ):
        source_path = os.path.join( source_dir, str( f[ 1 ] ) )
        dst_path = os.path.join( destination_dir, f"{i:04}.jpg" )
        # print( f"{source_path} -> {dst_path}" )
        shutil.move( source_path, dst_path )  

def load_json_files(directory_path, suffix=".jpg.json"):
    json_files = []
    for filename in os.listdir(directory_path):
        if filename.endswith(suffix):
            json_files.append(filename)
    return json_files

def load_json_from_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def loadAllMetadata( json_file ):
    all_data = {}

    for file in json_file:
        fp = os.path.join( ".", file )
        data = load_json_from_file( fp )
        all_data[ int( data[ "photoTakenTime" ][ "timestamp" ] ) ] =\
            data[ "title" ]

    sorted_list = sorted( all_data.items(), key=lambda item: item[ 0 ] )
    """
    print( "SORTED OUTPUT" )
    for items in sorted_list:
        print( f"Filename: {items[1]}, ts: {items[0]}" )
    """

    return sorted_list

def main():
    # Use a relative path based on the current working directory of the script
    relative_directory_path = "."  # Replace this with the actual relative path
    json_files_list = load_json_files(relative_directory_path)
    
    """
    print("JSON Files:")
    for json_file in json_files_list:
        print(json_file)
    """

    # Need to go through the list of json files, and pull out the necessary
    # info for sorting the photos by date. 
    sorted_data = loadAllMetadata( json_files_list )

    move_files( sorted_data, ".", "./processed" )

if __name__ == "__main__":
    main()
