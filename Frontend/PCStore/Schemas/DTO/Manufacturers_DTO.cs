using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    class Manufacturers_DTO
    {
        [JsonProperty]
        public string name { get; set; }
    }
}
