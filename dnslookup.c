#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netdb.h>

#define BUFLEN 256

int main(int argc, char *argv[]){

  int                      i;
  char                    *buf = malloc(BUFLEN);
  struct addrinfo          hints, *ai;
  void                     *ptr;



  if (argc != 2) {
    printf("Usage: %s <hostname>\n", argv[0]);
    return 1;
  }

  // Look up the IP address of the hostname specified on the command line
  memset(&hints, 0, sizeof(hints));
  hints.ai_family    = PF_UNSPEC;
  hints.ai_socktype  = SOCK_STREAM;
  if ((i = getaddrinfo(argv[1], NULL, &hints, &ai)) != 0) {
    printf("Unable to look up IP address: %s\n", gai_strerror(i));
    return 2;
  }

  while (ai){

    inet_ntop ( ai->ai_family, ai->ai_addr->sa_data, buf, BUFLEN);


    switch(ai->ai_family){

      case AF_INET:
         ptr = &((struct sockaddr_in *) ai->ai_addr)->sin_addr;
         break;
      case AF_INET6:
         ptr = &((struct sockaddr_in6 *) ai->ai_addr)->sin6_addr;
         break;

    }

    inet_ntop(ai->ai_family,ptr,buf,BUFLEN);
    if(ai->ai_family == PF_INET6){
      printf("%s IPv6 %s\n",argv[1],buf);
    }else{
      printf("%s IPv4 %s\n",argv[1],buf);
    }
    ai = ai->ai_next;
  }



}
