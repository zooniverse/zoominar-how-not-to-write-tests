#!/usr/bin/env ruby

class Solution
  attr_reader :boxes, :cars

  def done?(boxes)
    boxes.all? do |box|
      box == desired
    end
  end

  def desired
    sum = 0
    for stack_size in boxes
      sum += stack_size
    end

    desired = sum / cars
  end

  def run

    puts "-------"
    @cars = gets.to_i
    @boxes = gets.split(" ").map(&:to_i)
    puts @boxes.inspect

    maximum = (cars - 1) * 4
    puts maximum

    last_index = cars - 1
    for i in 0..(cars - 1)
      if !done?(boxes[i..-1])
        last_index = i
      end
    end
    puts 'desired', desired
    puts 'last index', last_index


    first_index = cars - 1
    for i in 0..(cars - 1)
      if !done?(boxes[0..i])
        first_index = i
      end
    end
    puts 'first index', first_index

    # puts boxes.inspect


    # grabbed = 0
    # for stack in boxes
    #   if stack > desired
    #     grabbed += (stack - desired)
    #   end
    # end

    # puts grabbed
  end
end

runs = gets.to_i
runs.times do
  Solution.new.run
end
