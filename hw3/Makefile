CC = gcc
CFLAGS = -Wall -Werror -fPIC
LDFLAGS = -shared
TARGET = libpmu.so
SOURCES = cycletime.c
OBJECTS = $(SOURCES:.cpp=.o)

libpmu:
	$(CC) -o libpmu.so cycletime.o $(LDFLAGS)

cycletime:
	$(CC) $(CFLAGS) -o cycletime.o -c cycletime.c

clean:
	rm -f $(OBJECTS) $(TARGET)
