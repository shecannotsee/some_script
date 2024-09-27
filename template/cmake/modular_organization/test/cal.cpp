#include <gtest/gtest.h>
#include <cal.h>

TEST(cal, add) {
  EXPECT_EQ(cal<int>::add(2,3), 5);
}