CC = gcc
LOADLIBES =  -L/usr/local/lib -lgsl -lgslcblas -lm
CFLAGS = -g -I/usr/local/include
OBJS = integration.o top.o converted_tops.o
DEPS = integration.h top.h converted_tops.h#$(LIBODE) # Makefile

PIC = -fPIC

#gaussian: gaussian.c
#	gcc $(CFLAGS) gaussian.c -o gaussian.o $(LOADLIBES)


inertia: inertia.o $(OBJS)
	$(CC) $(CFLAGS)  $(PIC) -Wall $(INCLUDE)  $^ -o $@ $(LOADLIBES)

%:%.o $(OBJS)#	 $(DEPS)
	$(CC) $(CFLAGS)  $(PIC) -Wall $(INCLUDE)  $^   -o $@ $(LOADLIBES)

%.o:%.c $(DEPS)
		$(CC) $(CFLAGS) -c  $(PIC) -Wall $(INCLUDE)  $< -o $@ #$(LOADLIBES)

#$(LIBODE): $(OBJS)
#	ar -cr $@  $?

clean:
	rm -rf *.so *.dylib *.o *~ *.a
