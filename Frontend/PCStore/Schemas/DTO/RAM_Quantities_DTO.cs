﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    internal class RAM_Quantities_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("ram_number")]
        public string Ram_Number { get; set; }
    }
}
