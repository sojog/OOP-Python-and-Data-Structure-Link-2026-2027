from TimeConverterWithProperties import TimeConverter

t0 = TimeConverter(4, 56)
print(t0)

print(t0.to_minutes)
print(t0.to_hours)

print(t0 + t0)
print(t0 - t0)