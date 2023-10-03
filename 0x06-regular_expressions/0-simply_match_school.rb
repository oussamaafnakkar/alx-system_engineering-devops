#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

# Input string from the command line argument
input_string = ARGV[0]

# Regular expression pattern
pattern = /School/

# Perform the regular expression match
if match = input_string.match(pattern)
  puts match[0]
else
  puts ""
end
