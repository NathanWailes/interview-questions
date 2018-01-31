using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Text;
using Newtonsoft.Json;
using System.Linq;

namespace olo_code_test
{
    internal class Item
    {
        [JsonProperty("toppings")]
        public string[] Toppings { get; set; }
    }
    class Program
    {
        static void Main(string[] args)
        {
            // Assemble the request to the API
            HttpWebRequest webReq = (HttpWebRequest)WebRequest.Create(string.Format("http://files.olo.com/pizzas.json"));
            webReq.Method = "GET";

            // Get the response
            HttpWebResponse webResp = (HttpWebResponse)webReq.GetResponse();

            // Extract the JSON string from the response
            string jsonString;
            using (Stream stream = webResp.GetResponseStream())
            {
                StreamReader reader = new StreamReader(stream, System.Text.Encoding.UTF8);
                jsonString = reader.ReadToEnd();
            }

            // Convert the JSON string into a List object
            List<Item> items = JsonConvert.DeserializeObject<List<Item>>(jsonString);

            // Create an empty frequency counter
            Dictionary<string, int> toppingFrequencyCounter = new Dictionary<string, int>();

            // Fill in the frequency counter with the data from the List object.
            foreach (var item in items) {
                // First generate a unique key based on the names of the chosen toppings.

                // Sort the list of toppings so that we'll always generate the same key from the same list of toppings.
                Array.Sort(item.Toppings, StringComparer.InvariantCulture);
                
                // Combine the toppings names to create the key
                string frequencyCounterKey = String.Join("|$|", item.Toppings);

                // If this topping combination hasn't been added to the frequency dict yet...
                if (!toppingFrequencyCounter.ContainsKey(frequencyCounterKey)) {
                    toppingFrequencyCounter[frequencyCounterKey] = 1;
                } else {
                    // If we've already seen this combination, increment the count.
                    int existingCount = toppingFrequencyCounter[frequencyCounterKey];
                    toppingFrequencyCounter[frequencyCounterKey] = existingCount + 1;
                }
            }

            // Sort the frequency counter by count
            var sortedFreqCounter = from entry in toppingFrequencyCounter orderby entry.Value descending select entry;

            // Print the top 20 most popular topping combinations.
            int i = 1;
            foreach (var item in sortedFreqCounter) {
                // Create a comma-separated string of the toppings
                String[] individualToppings = item.Key.Split("|$|");
                string toppingsString = String.Join(", ", individualToppings);

                // Print to the console
                Console.WriteLine("{0,3}{1,40}{2,6}", i, toppingsString, item.Value);

                i++;
                if (i > 20) {
                    break;
                }
            }
        }
    }
}
