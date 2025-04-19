using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    internal class Base_Material_DTO
    {
        [JsonProperty("id")]
        public string Id { get; set; }

        [JsonProperty("material")]
        public string Material { get; set; }
    }
}
