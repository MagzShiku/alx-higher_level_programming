#include "lists.h"
/**
 * insert_node - a function that inserts nodes in a stringly linked list
 * @head: the entry into the list
 * @number: the number being inserted
 * Return: Address of the new node 'nodeX' and NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodeX = malloc(sizeof(listint_t));
	listint_t *present_node = *head;

	if (nodeX == NULL)
	{
		return (NULL);
	}

	nodeX->n = number;
	nodeX->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		nodeX->next = *head;
		*head = nodeX;
	}
	else
	{
		while (present_node->next != NULL && present_node->next->n <= number)
		{
			present_node = present_node->next;
		}
		nodeX->next = present_node->next;
		present_node->next = nodeX;
	}
return (nodeX);
}
