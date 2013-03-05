#include "dblist.h"

list *listCreate() {
  list *lst = (list *) malloc (sizeof(list));
  if (lst == NULL) return NULL;
  lst->head = NULL;
  lst->tail = NULL;
  lst->free = NULL;
  lst->len = 0;
  return lst;
}

void listFree(list *lst) {
  listIter *iter = listCreateIterFromHead(lst);
  listNode* current = listNext(iter);
  while (current != NULL) {
    if (lst->free) lst->free(current->value);
    lst->len -= 1;
    free(current);
    current = listNext(iter);
  }
  listFreeIter(iter);
  free(lst);
}

listIter *listCreateIter(list *lst, int dir) {
  listIter *iter = (listIter*) malloc (sizeof(listIter));
  if (iter == NULL) return NULL;
  if (dir == LIST_ITER_FROM_HEAD) 
    iter->next = lst->head;
  else
    iter->next = lst->tail;
  iter->dir = dir;
  return iter;
}


listNode *listNext(listIter *iter) {
  listNode *current = iter->next;
  if (current != NULL) {
    if (iter->dir == LIST_ITER_FROM_HEAD) {
      iter->next = current->next;
    } else {
      iter->next = current->prev;
    }
  }
  return current;
}

listNode *listAddNodeHead(list *lst, void *value) {
  listNode *new_node = (listNode *)malloc(sizeof(listNode));
  if (new_node == NULL) return NULL;
  new_node->value = value;
  if (lst->len == 0) {
    new_node->prev = new_node->next = NULL;
    lst->head = lst->tail = new_node;
  } else {
    new_node->next = lst->head;
    new_node->prev = NULL;
    lst->head = new_node;
  }
  lst->len+=1;
  return new_node;
}
listNode *listAddNodeTail(list *lst, void *value) {
  listNode *new_node = (listNode *)malloc(sizeof(listNode));
  if (new_node == NULL) return NULL;
  new_node->value = value;
  if (lst->len == 0) {
    new_node->prev = new_node->next = NULL;
    lst->head = lst->tail = new_node;
  } else {
    new_node->prev = lst->tail;
    new_node->next = NULL;
    lst->tail = new_node;
  }
  lst->len+=1;
  return new_node;
}

list *listInsertNode(list *list, listNode *old_node, void *value, int after) {
  listNode *new_node = (listNode *)malloc(sizeof(listNode));
  if (new_node == NULL) return NULL;
  new_node->value = value;
  if (after) {
    new_node->next = old_node->next;
    new_node->prev = old_node;
    if (old_node->next) {
      old_node->next->prev = new_node;
    }
    old_node->next = new_node;
  } else {
    new_node->next = old_node;
    new_node->prev = old_node->prev;
    if (old_node->prev) {
      old_node->prev->next = new_node;
    }
    old_node->prev = new_node;
  }
  lst->len+=1;
  return list;
}
list *listDelNode(list *list, listNode *node) {
  if (node->prev == NULL && node->next == NULL) {  // del head and tail
    list->head = list->tail = NULL;
  } else if (node->prev == NULL) { // del head
    node->next->prev = node->prev;
    list->head = node->next;
  } else if (node->next == NULL) { // del tail
    node->prev->next = node->next;
    list->tail = node->prev;
  } else {
    node->next->prev = node->prev;
    node->prev->next = node->next;
  }
  if (list->free) list->free(node->value);
  free(node);
  list->len-=1;
  return list;
}
