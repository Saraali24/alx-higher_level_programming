#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"


/**
 * insert_node - inserts number into a sorted singly linked list
 * @head: pointer to first node
 * @number: data in new node
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *current_ptr;

current_ptr = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

new->n = number;
new->next = NULL;

if (*head == NULL)
{
*head = new;
return (new);
}
else
{
if (current_ptr->n > number)
{
new->next = current_ptr;
*head = new;
return (new);
}
while (current_ptr->next != NULL)
{
if (current_ptr->next->n > number)
{
new->next = current_ptr->next;
current_ptr->next = new;
return (new);
}
current_ptr = current_ptr->next;
}
}
current_ptr->next = new;
return (new);
}
