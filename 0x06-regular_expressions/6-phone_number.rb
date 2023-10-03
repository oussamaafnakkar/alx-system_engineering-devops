#!/usr/bin/env ruby

# Use scan to find all matches of exactly 10 digits and join them
matches = ARGV[0].scan(/^\d{10,10}$/)

# Display the matches (joined together if multiple)
puts matches.join
