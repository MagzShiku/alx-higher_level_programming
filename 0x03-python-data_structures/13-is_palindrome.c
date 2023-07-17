#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * is_palindrome - a function that checks for palindrome, intereting
 * @head: The first node of the list
 * Return: 0 if not a palindrome, 1 if it is
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *hare;/*moves two nodes at a time*/
	listint_t *tortoise;/*moves one node at a time*/
	listint_t *formor;/*helps reverse the list*/
	listint_t *next;/*helps reverse the list*/

	hare = *head;
	tortoise = *head;
	formor = NULL;
	next = NULL;

	if (*head == 0 || (*head)->next == 0)
	{
		return (1);
	/*checks to see if the empty string is there,if yes, its a palindrome*/
	}

	while (hare && hare->next)
	{
		hare = hare->next->next;
		next = tortoise->next;
		tortoise->next = formor;
		formor = tortoise;
		tortoise = next;
	}

	if (hare)
	{
		tortoise = tortoise->next;
	}

	while (formor && tortoise)
	{
		if (formor->n != tortoise->n)
		{
			return (0);
		}
		formor = formor->next;
		tortoise = tortoise->next;
	}
	return (1);
}
