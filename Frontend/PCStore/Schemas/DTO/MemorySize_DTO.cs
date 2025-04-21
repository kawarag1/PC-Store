using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    public class MemorySize_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("size")]
        public int Size { get; set; }
    }
}
