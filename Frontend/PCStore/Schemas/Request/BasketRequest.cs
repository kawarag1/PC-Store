using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PCStore.Schemas.Request
{
    public class BasketRequest
    {
        public int id { get; set; }

        public string? article { get; set; }
    }
}
