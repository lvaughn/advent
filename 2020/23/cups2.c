#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  struct Node* next;
};

struct Node* init() {
  //int values[] = {3, 8, 9, 1, 2, 5, 4, 6, 7};
  int values[] = {1, 2, 3, 4, 8, 7, 5, 9, 6};
  struct Node* start = (struct Node*) malloc (sizeof(struct Node));
  start->data = values[0];
  struct Node *curr = start;
  for(int i=1; i < 9; i += 1) {
	struct Node* new_node =  (struct Node*) malloc (sizeof(struct Node));
	new_node->data = values[i];
	curr->next = new_node;
	curr = new_node;
  }
  curr->next = start;
  return start;
}

int find_max(struct Node* ls) {
  struct Node* start = ls;
  int max = ls->data;
  ls = ls->next;
  while(ls != start) {
	if (ls->data > max) {
	  max = ls->data;
	}
	ls = ls->next;
  }
  return max;
}

void printList(struct Node* ls) {
    struct Node* start = ls;
    do {
        printf("%d", ls->data);
        ls = ls->next;
    } while(ls != start);
    printf("\n");
}

struct Node* runRound(struct Node* ls, int size) {
    //printList(ls);
    int current = ls->data;
    struct Node* start = ls;
    struct Node* toRemove = ls->next;
    ls->next = ls->next->next->next->next;
    //printList(ls);
    int a = toRemove->data;
    int b = toRemove->next->data;
    int c = toRemove->next->next->data;
    int insertTarget = current - 1;
    if (insertTarget == 0) insertTarget = size;
    //printf("LGV:a,%d,%d,%d:%d\n", a, b, c, current);
    while ((insertTarget == a) || (insertTarget == b) || (insertTarget == c)) {
        --insertTarget;
        if (insertTarget == 0) insertTarget = size;
    }
    struct Node* insertPoint = ls->next;
    //printf("LGV:b:%d\n", insertTarget);
    while (insertPoint->data != insertTarget) insertPoint = insertPoint->next;
    //printf("LGV:c:%d:%d\n", insertPoint->data, toRemove->next->next->data);
    toRemove->next->next->next = insertPoint->next;
    insertPoint->next = toRemove;
    //printList(ls->next);
    return ls->next;
}

void printFromOne(struct Node* ls) {
    while (ls->data != 1) ls = ls->next;
    struct Node* one = ls;
    ls = ls->next;
    while(ls != one) {
        printf("%d", ls->data);
        ls = ls->next;
    }
    printf("\n");
}
  

int main() {
  struct Node* start = init();
  int maxValue = find_max(start);
  printf("Max value: %d\n", maxValue);
  printFromOne(start);
  for(int i=0; i != 100; i++) {
    start = runRound(start, maxValue);
  }
  printFromOne(start);
}

	
