#!/usr/bin/env ruby
# {{{
require 'rubygems'
require 'bundler/inline'

gemfile do
  source 'https://rubygems.org'
  gem 'rspec'
  gem 'approvals'
end
# }}}

def a_complicated_operation
  [1,2,37,42]
end

require 'approvals/rspec'

describe 'Complicated Operation' do
  it 'does something in a certain case' do
    verify do
      a_complicated_operation
    end
  end
end