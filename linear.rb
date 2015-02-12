def get_function s
  return Proc.new{|n| ((s[1]-s[0])*n)+ s[0]}
end
p get_function([0, 1, 2, 3, 4]).call(5)
p get_function([0, 3, 6, 9, 12]).call(10)
p get_function([1, 4, 7, 10, 13]).call(20)