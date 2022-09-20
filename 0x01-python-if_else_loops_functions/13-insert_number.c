#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"
/**
 * *insert_node - Adds node at end of list
 * @head: The head of the list
 * @number: The number to be added
 * 
 * Return: A pointer to the list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;

	if (head != NULL)
	{
		temp = malloc(sizeof(listint_t));
		if (temp == NULL)
			return (NULL);

		temp->number = strdup(number);
		temp->number = strlen(number);
		temp->next = *head;

		*head = temp;

		return (temp);
	}
}