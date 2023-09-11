#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node
 * Return: 0
 */

int is_palindrome(listint_t **head)
{
listint_t *ptr = *head;
listint_t *temp = *head;
listint_t *prev = NULL;
listint_t *next;

if (!head || !*head || !(*head)->next)
return (1);

while (temp != NULL && temp->next != NULL)
{
temp = temp->next->next;
next = ptr->next;
ptr->next = prev;
prev = ptr;
ptr = next;
}

if (temp != NULL)
{
ptr = ptr->next;
}

while (prev != NULL && ptr != NULL)
{
if (prev->n != ptr->n)
return (0);

prev = prev->next;
ptr = ptr->next;
}

return (1);
}
