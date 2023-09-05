#include "lists.h"

/**
 * insert_node - inserts a new value such that list still sorted
 * @head: pointer to the list head
 * @number: the new number to be added
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c = *head, *p, *newnode;

	newnode = malloc(sizeof(struct listint_s));
	newnode->n = number;

	if (!(*head) && (*head)->n > number)
	{
		newnode->next = *head;
		*head = newnode;
		return (*head);
	}

	while (c && c->n < number)
	{
		p = c;
		c = c->next;
	}

	if (!c)
	{
		p->next = newnode;
		newnode->next = NULL;
	}
	else
	{
		p->next = newnode;
		newnode->next = c;
	}
	return (newnode);
}
