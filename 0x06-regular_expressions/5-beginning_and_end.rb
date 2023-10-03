#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

# Input string from the command line argument
input_string = ARGV[0]

# Regular expression pattern
pattern = /^h.n$/

# Perform the regular expression match
if pattern.match?(input_string)
  puts input_string
else
  puts ""
end
