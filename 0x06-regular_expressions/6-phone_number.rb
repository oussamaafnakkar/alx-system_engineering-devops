#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: #{$0} <phone_number>"
  exit 1
end

# Input phone number from the command line argument
phone_number = ARGV[0]

# Regular expression pattern for a 10-digit phone number
pattern = /^\d{10}$/

# Perform the regular expression match
if pattern.match?(phone_number)
  puts phone_number
else
  puts ""
end
