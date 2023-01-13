<script lang="ts">
	import axios from 'axios';
	import { text } from 'svelte/internal';
  
	let textInput: string = '';
	let responseText: string | null = null;
  
	async function handleSubmit() {
	  try {
		const formData = new FormData();
    	formData.append('text', textInput);
		const response = await axios.post('api/open-ai/', formData);
		responseText = response.data.replace(/<br\s*[\/]?>/gi, "\n");
		// responseText = response.data;
		console.log(responseText)
	  } catch (error) {
		console.error(error);
	  }
	}
  </script>
<head>
	<title>Hamburger Meat Recipe</title>
	<style>
		body {
			font-family: Arial, sans-serif;
			margin: 0;
			padding: 0;
		}
		.recipe-container {
			max-width: 800px;
			margin: 0 auto;
			padding: 20px;
			box-sizing: border-box;
		}
		.recipe-title {
			text-align: center;
			font-size: 32px;
			font-weight: bold;
			margin-bottom: 20px;
			color: #333;
		}
		.ingredients, .instructions {
			width: 100%;
			border-collapse: collapse;
			margin-bottom: 20px;
		}
		.ingredients th, .instructions th {
			background-color: #333;
			color: #fff;
			font-size: 16px;
			padding: 10px;
			text-align: left;
		}
		.ingredients td, .instructions td {
			padding: 10px;
			font-size: 14px;
			border-bottom: 1px solid #ccc;
		}
		.ingredients td:first-child {
			font-weight: bold;
			width: 30%;
		}
		.instructions ol {
			padding-left: 20px;
			margin: 0;
		}
		.instructions ol li {
			margin-bottom: 10px;
			font-size: 14px;
		}
		#text-input {
			min-width: 200px;
		}
		pre {
  			max-width: 400px;
		}

	</style>
</head>
<body>
	<div class="recipe-container">
		<h1 class="recipe-title">Recipe Requester</h1>
		  <form on:submit|preventDefault={handleSubmit}>
			<label for="text-input">What would you like to find a recipe for?:</label>
			<input type="text" id="text-input" bind:value={textInput} />
			<button type="submit">Submit</button>
		  </form>
		  {#if responseText}
			<pre>{responseText}</pre>
		  {/if}
		<h1 class="recipe-title">Hamburger Meat Recipe</h1>
		<table class="ingredients">
			<tr>
				<th>Ingredient</th>
				<th>Amount</th>
			</tr>
			<tr>
				<td>Ground beef</td>
				<td>500 grams</td>
			</tr>
			<tr>
				<td>Salt</td>
				<td>1/2 teaspoon</td>
			</tr>
			<tr>
				<td>Black pepper</td>
				<td>1/4 teaspoon</td>
			</tr>
			<tr>
				<td>Garlic powder</td>
				<td>1/4 teaspoon</td>
			</tr>
			<tr>
				<td>Onion powder</td>
				<td>1/4 teaspoon</td>
			</tr>
			<tr>
				<td>Worcestershire sauce</td>
				<td>2 tablespoons</td>
			</tr>
		</table>
		<table class="instructions">
			<tr>
				<th>Instructions</th>
			</tr>
			<tr>
				<td>
					<ol>
						<li>Place ground beef in a large mixing bowl.</li>
						<li>Add salt, black pepper, garlic powder, and onion powder to the bowl.</li>
						<li>Pour Worcestershire sauce into the bowl.</li>
						<li>Use your hands to mix all of the ingredients together until well combined.</li>
						<li>Use a knife to divide the mixture into 4 equal portions.</li>
						<li>Shape each portion into a patty that is about 1/2 inch thick.</li>
						<li>Preheat a grill or stovetop griddle pan over medium-high heat.</li>
						<li>Place the patties on the grill or griddle pan and cook for 3-4 minutes on each side, or until the internal temperature reaches 160°F. Use tongs or a spatula to flip the patties.</li>
						<li>Serve the hamburger patties on buns with your desired toppings. Enjoy!</li>
					</ol>
				</td>
			</tr>
		</table>
	</div>
</body>

  

  