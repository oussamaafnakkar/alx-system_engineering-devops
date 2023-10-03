#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

# Input string from the command line argument
input_string = ARGV[0]

# Use scan to find all matches and join them
matches = input_string.scan(/^h.n$/)

# Display the matches (joined together if multiple)
puts matches.join
