// Double linked list


#ifndef DBLIST_LXJL2L4R

#define DBLIST_LXJL2L4R

typedef struct listNode {
  listNode *prev;
  listNode *next;
  void *value;
} listNode;

typedef struct listIter {
  listNode *next;
  int dir;
} listIter;

typedef struct list {
  listNode *head;
  listNode *tail;
  void (*free)(void *ptr);
  unsigned long len;
} list;

#define listSetFreeMethod(l, (m)) ((l)->free = (m))

list *listCreate();
void listFree(list *lst);
listNode *listAddNodeHead(list *list, void *value);
listNode *listAddNodeTail(list *list, void *value);
listIter *listCreateIter(list *list, int dir);
void listFreeIter(listIter *iter);
listNode *listNext(listIter *iter);
list *listInsertNode(list *list, listNode *old_node, void *value, int after);
list *listDelNode(list *list, listNode *node);

#define LIST_ITER_FROM_HEAD 0
#define LIST_ITER_FROM_TAIL 1

#endif /* end of include guard: DBLIST_LXJL2L4R */
